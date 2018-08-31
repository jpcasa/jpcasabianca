import Vuex from 'vuex'
import menus from './modules/menus'
import skills from './modules/skills'

const createStore = () => {
  return new Vuex.Store({
     modules: {
       menus,
       skills
     }
  })
}

export default createStore
