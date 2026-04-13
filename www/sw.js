const CACHE_NAME = 'bk-bank-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/png/изображение_2025-02-11_142359079.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
