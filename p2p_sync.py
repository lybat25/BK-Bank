import json
import sqlite3
import threading
import time
import hashlib
from datetime import datetime
from queue import Queue
from flask import jsonify

try:
    from gun import Gun
except ImportError:
    print("❌ Установи gun: pip install gun")
    raise

class P2PManager:
    def __init__(self, db_path='database.db', peer_id=None):
        self.db_path = db_path
        self.peer_id = peer_id or self._generate_peer_id()
        self.gun = None
        self.user_ref = None
        self.sync_queue = Queue()
        self.connected_peers = set()
        self.running = False
        self.local_changes = {}
        self.sync_thread = None
        
        print(f"🆔 Твой Peer ID: {self.peer_id}")
        print(f"📱 Для подключения другого устройства используй этот код")
        
    def _generate_peer_id(self):
        import uuid
        return str(uuid.uuid4())[:8]
    
    def start(self):
        if self.running:
            return
        
        self.running = True
        
        self.gun = Gun([
            'https://gun-manhattan.herokuapp.com/gun',
            'https://gun-us.herokuapp.com/gun',
            'https://gun-eu.herokuapp.com/gun'
        ])
        
        self.user_ref = self.gun.user(self.peer_id)
        
        self._subscribe_to_changes()
        
        self.sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
        self.sync_thread.start()
        
        print(f"🌐 P2P синхронизация запущена")
        print(f"📡 Твой Peer ID: {self.peer_id}")
        
    def _subscribe_to_changes(self):
        def on_change(data, key, msg, event):
            if not data:
                return
            
            try:
                self._apply_remote_changes(data)
            except Exception as e:
                print(f"❌ Ошибка применения изменений: {e}")
        
        sync_channel = self.user_ref.get('bk_bank_sync')
        sync_channel.map().on(on_change)
        
    def _apply_remote_changes(self, data):
        if not isinstance(data, dict):
            return
        
        operation = data.get('op')
        table = data.get('table')
        values = data.get('values')
        conditions = data.get('conditions')
        
        if not operation or not table:
            return
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            if operation == 'INSERT':
                placeholders = ','.join(['?' for _ in values])
                columns = ','.join(values.keys())
                cursor.execute(
                    f"INSERT OR REPLACE INTO {table} ({columns}) VALUES ({placeholders})",
                    list(values.values())
                )
                
            elif operation == 'UPDATE':
                set_clause = ','.join([f"{k}=?" for k in values.keys()])
                where_clause = ' AND '.join([f"{k}=?" for k in conditions.keys()])
                cursor.execute(
                    f"UPDATE {table} SET {set_clause} WHERE {where_clause}",
                    list(values.values()) + list(conditions.values())
                )
                
            elif operation == 'DELETE':
                where_clause = ' AND '.join([f"{k}=?" for k in conditions.keys()])
                cursor.execute(
                    f"DELETE FROM {table} WHERE {where_clause}",
                    list(conditions.values())
                )
            
            conn.commit()
            print(f"✅ Применено удаленное изменение: {operation} в {table}")
            
        except Exception as e:
            print(f"❌ Ошибка SQL при применении изменений: {e}")
        finally:
            conn.close()
    
    def _sync_loop(self):
        while self.running:
            try:
                change = self.sync_queue.get(timeout=1)
                
                sync_channel = self.user_ref.get('bk_bank_sync')
                sync_channel.set(change)
                
                print(f"📤 Отправлено в P2P: {change.get('op')} в {change.get('table')}")
                
            except Exception as e:
                if "Empty" not in str(e):
                    print(f"⚠️ Ошибка синхронизации: {e}")
                continue
    
    def sync_insert(self, table, values):
        change = {
            'op': 'INSERT',
            'table': table,
            'values': values,
            'timestamp': datetime.utcnow().isoformat(),
            'peer_id': self.peer_id
        }
        self.sync_queue.put(change)
        
    def sync_update(self, table, values, conditions):
        change = {
            'op': 'UPDATE',
            'table': table,
            'values': values,
            'conditions': conditions,
            'timestamp': datetime.utcnow().isoformat(),
            'peer_id': self.peer_id
        }
        self.sync_queue.put(change)
        
    def sync_delete(self, table, conditions):
        change = {
            'op': 'DELETE',
            'table': table,
            'conditions': conditions,
            'timestamp': datetime.utcnow().isoformat(),
            'peer_id': self.peer_id
        }
        self.sync_queue.put(change)
    
    def stop(self):
        self.running = False
        if self.sync_thread:
            self.sync_thread.join(timeout=2)
        print("🛑 P2P синхронизация остановлена")

p2p = None

def init_p2p(peer_id=None):
    global p2p
    if p2p is None:
        p2p = P2PManager(peer_id=peer_id)
        p2p.start()
    return p2p

def get_p2p():
    return p2p
