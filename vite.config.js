import { defineConfig } from 'vite';
const { resolve } = require('path');

// https://vitejs.dev/config/
export default defineConfig({
  base: '/Telegram-Search-Bot/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
    },
  },
});
