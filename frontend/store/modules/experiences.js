// initial state
// shape: [{ id, quantity }]
const state = {
  experiences: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setExperience: (state, experiences) => {
    state.experiences = experiences
  }
}

// actions
const actions = {
  async getExperience ({commit}) {
    const data = await this.$axios.$get(`experiences/?format=json`)
    commit('setExperience', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
