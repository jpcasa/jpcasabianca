// initial state
// shape: [{ id, quantity }]
const state = {
  menus: [],
  menu: {},
  subMenu: {},
  contactMenu: {},
  menuActive: "",
  subMenuActive: 0,
  footer1: {},
  footer2: {},
  socialMenu: {}
}

// getters
const getters = {}

// mutations
const mutations = {
  setMenus: (state, menus) => {
    state.menus = menus
  },
  setMainMenu: (state, menu) => {
    state.menu = menu
  },
  setSubMenu: (state, subMenu) => {
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
  setSubMenuClick: (state, id) => {
    state.subMenu = state.menu.menu_items[id].sub_menu_items
  },
  setFooter1: (state, footer1) => {
    state.footer1 = footer1
  },
  setFooter2: (state, footer2) => {
    state.footer2 = footer2
  },
  setSocialMenu: (state, socialMenu) => {
    state.socialMenu = socialMenu
  }
}

// actions
const actions = {
  async getMenus ({commit}) {
    const data = await this.$axios.$get(`menus/?format=json`)
    commit('setMenus', data)
  },
  async getMainMenu ({commit}, path) {
    const data = await this.$axios.$get(`menus/1/?format=json`)
    let path_name = ''
    if (path != '/') {
      path_name = path.split("/")
      path_name = path_name[1]
    } else {
      path_name = ''
    }
    const active_item = data.menu_items.filter(item => item.url == path_name)
    const active_item_id = active_item[0].id - 1
    commit('setMainMenu', data)
    commit('setMenuActive', data.menu_items[active_item_id].url)
    if (data.menu_items[active_item_id].sub_menu_items.length) {
      commit('setSubMenu', data.menu_items[active_item_id].sub_menu_items)
      commit('setSubMenuActive', data.menu_items[active_item_id].sub_menu_items[0].id)
    }
  },
  async getContactMenu ({commit}) {
    const data = await this.$axios.$get(`menus/2/?format=json`)
    commit('setContactMenu', data)
  },
  async assignMenuActive ({commit}, url) {
    commit('setMenuActive', url)
  },
  async getSubMenu ({commit}, id) {
    commit('setSubMenuClick', (id - 1))
    commit('setSubMenuActive', id)
  },
  async getFooterMenus ({commit}) {
    const data1 = await this.$axios.$get(`menus/3/?format=json`)
    const data2 = await this.$axios.$get(`menus/4/?format=json`)
    commit('setFooter1', data1)
    commit('setFooter2', data2)
  },
  async getSocialMenu ({commit}) {
    const data = await this.$axios.$get(`menus/5/?format=json`)
    commit('setSocialMenu', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
