import { createStore } from 'vuex'
import imageStore from './image'
import nendoroidsStore from './nendoroids'
import utilsStore from './utils'

export default createStore({
  namespaced: true,
  modules: {
    imageStore,
    nendoroidsStore,
    utilsStore
  }
})