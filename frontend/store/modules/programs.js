// initial state
// shape: [{ id, quantity }]
const state = {
  programs: [],
  categories: [],
  programs_cat: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setPrograms: (state, programs) => {
    state.programs = programs
  },
  setProgramCategories: (state, categories) => {
    state.categories = categories
  },
  setProgramsCat: (state, programs_cat) => {
    state.programs_cat = programs_cat
  }
}

// actions
const actions = {
  async getPrograms ({commit}) {
    const data = await this.$axios.$get(`programs/?format=json`)
    commit('setPrograms', data)
  },
  async getProgramCategories ({commit}) {
    const data = await this.$axios.$get(`program-categories/?format=json`)
    commit('setProgramCategories', data)
  },
  async getProgramsCat ({commit}, url) {
    const data = await this.$axios.$get(`programs/search/${url}/?format=json`)
    commit('setProgramsCat', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
