import { defineConfig } from 'vite';
const { resolve } = require('path');

// https://vitejs.dev/config/
export default defineConfig({
  base: '/Bridge-of-Liberty/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
      },
    },
  },
});
