import Vuex from 'vuex'

const createStore = () => {
  return new Vuex.Store({
    state: {
      menus: [],
      menu: {},
      subMenu: {},
      contactMenu: {},
      menuActive: 0,
      subMenuActive: 0
    },
    mutations: {
      setMenus: (state, menus) => {
        state.menus = menus
      },
      setMainMenu: (state, menu) => {
        state.menu = menu
      },
      setSubMainMenu: (state, subMenu) => {
        state.subMenu = subMenu
      },
      setMenuActive: (state, menuActive) => {
        state.menuActive = menuActive
      },
      setSubMenuActive: (state, subMenuActive) => {
        state.subMenuActive = subMenuActive
      },
      setContactMenu: (state, contactMenu) => {
        state.contactMenu = contactMenu
      },
    },
    actions: {
      async getMenus ({commit}) {
        const data = await this.$axios.$get(`menus/?format=json`)
        commit('setMenus', data)
      },
      async getMainMenu ({commit}) {
        const data = await this.$axios.$get(`menus/1/?format=json`)
        commit('setMainMenu', data)
        commit('setMenuActive', data.menu_items[0].id)
        if (data.menu_items[0].sub_menu_items.length) {
          commit('setSubMainMenu', data.menu_items[0].sub_menu_items)
          commit('setSubMenuActive', data.menu_items[0].sub_menu_items[0].id)
        }
      },
      async getContactMenu ({commit}) {
        const data = await this.$axios.$get(`menus/2/?format=json`)
        commit('setContactMenu', data)
      },
    }
  })
}

export default createStore
