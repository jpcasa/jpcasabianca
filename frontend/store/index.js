import Vuex from 'vuex'
import menus from './modules/menus'
import skills from './modules/skills'
import experiences from './modules/experiences'
import programs from './modules/programs'
import education from './modules/education'
import portfolio from './modules/portfolio'
import testimonies from './modules/testimonies'


const createStore = () => {
  return new Vuex.Store({
     modules: {
       menus,
       skills,
       experiences,
       programs,
       education,
       portfolio,
       testimonies
     }
  })
}

export default createStore
