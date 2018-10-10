// initial state
// shape: [{ id, quantity }]
const state = {
  case_studies: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setCaseStudies: (state, case_studies) => {
    state.case_studies = case_studies
  }
}

// actions
const actions = {
  async getCaseStudies ({commit}) {
    const data = await this.$axios.$get(`case-studies/?format=json`)
    commit('setCaseStudies', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
