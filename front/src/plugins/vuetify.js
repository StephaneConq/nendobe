// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Vuetify
import { createVuetify } from 'vuetify'

export default createVuetify(
  // https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
  {
    theme: {
      defaultTheme: 'dark',
      themes: {
          dark: {
              dark: true,
              variables: {}, // ✅ this property is required to avoid Vuetify crash

              colors: {
                  primary: '#f39500',
                  secondary: '#ffffff',
                  accent: '#e101a0',
                  error: '#b71c1c',
              },
          }
      }
  }
  }
)
