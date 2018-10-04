import Vuex from 'vuex'
import menus from './modules/menus'
import skills from './modules/skills'
import experiences from './modules/experiences'
import programs from './modules/programs'
import education from './modules/education'


const createStore = () => {
  return new Vuex.Store({
     modules: {
       menus,
       skills,
       experiences,
       programs,
       education
     }
  })
}

export default createStore
