const CACHE_NAME = 'bk-bank-v2';
self.addEventListener('install', e => { self.skipWaiting(); e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(['/','/index.html','/manifest.json']))); });
self.addEventListener('fetch', e => { e.respondWith(fetch(e.request).then(r => { const rc = r.clone(); caches.open(CACHE_NAME).then(c => c.put(e.request, rc)); return r; }).catch(() => caches.match(e.request))); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(n => Promise.all(n.filter(nn => nn !== CACHE_NAME).map(nn => caches.delete(nn))))); });
