// initial state
// shape: [{ id, quantity }]
const state = {
  education: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setEducation: (state, education) => {
    state.education = education
  }
}

// actions
const actions = {
  async getEducation ({commit}) {
    const data = await this.$axios.$get(`education/?format=json`)
    commit('setEducation', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
