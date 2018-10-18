// initial state
// shape: [{ id, quantity }]
const state = {
  testimonies: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setTestimonies: (state, testimonies) => {
    state.testimonies = testimonies
  }
}

// actions
const actions = {
  async getTestimonies ({commit}) {
    const data = await this.$axios.$get(`testimonies/?format=json`)
    commit('setTestimonies', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
