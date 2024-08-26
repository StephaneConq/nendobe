import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'
import { VitePWA } from 'vite-plugin-pwa'

const path = require('path')

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        "theme_color": "#121212",
        "background_color": "#f39500",
        "icons": [
          {
            "purpose": "maskable",
            "sizes": "512x512",
            "src": "img/icons/icon512_maskable.png",
            "type": "image/png"
          },
          {
            "purpose": "any",
            "sizes": "512x512",
            "src": "img/icons/icon512_rounded.png",
            "type": "image/png"
          }
        ],
        "orientation": "portrait",
        "display": "standalone",
        "dir": "auto",
        "lang": "fr-FR",
        "name": "Nendobe",
        "short_name": "Nendobe",
        "start_url": "https://nendobe-pmvbal4k7a-od.a.run.app",
        "scope": "https://nendobe-pmvbal4k7a-od.a.run.app",
        "description": "Tracker le prix des Nendoroids"
      }
    }),
    vue(),
    // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
    vuetify({
      autoImport: true,
    }),
  ],
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  /* remove the need to specify .vue files https://vitejs.dev/config/#resolve-extensions
  resolve: {
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ]
  },
  */
})
