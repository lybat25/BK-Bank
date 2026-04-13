const CACHE_NAME = 'bk-bank-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/style.css',
  '/manifest.json',
  '/png/2025-01-30_15-13-31-Photoroom.png',
  '/png/2025-01-30_15-58-26-Photoroom.png',
  '/png/2025-01-30_21-48-25-Photoroom.png',
  '/png/2025-01-30_22-57-01-Photoroom.png',
  '/png/2025-01-30_23-01-20-Photoroom.png',
  '/png/2025-01-30_23-05-01-Photoroom.png',
  '/png/2025-01-30_23-06-40-Photoroom.png',
  '/png/2025-01-30_17-50-13-Photoroom.png',
  '/png/2025-01-31_14-13-47-Photoroom.png'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const clonedResponse = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, clonedResponse);
        });
        return response;
      })
      .catch(() => {
        return caches.match(event.request);
      })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
});
