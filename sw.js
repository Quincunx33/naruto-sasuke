const CACHE_NAME = 'naruto-v1';
const ASSETS = [
  './',
  './index.html',
  './assets/naruto.mp4',
  './assets/sasuke.mp4',
  './assets/naruto_dialogue.wav',
  './assets/sasuke_dialogue.wav',
  './assets/naruto_bgm.mp3',
  './assets/rasengan_sfx.mp3',
  './assets/chidori_sfx.mp3'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
});

self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request)));
});
