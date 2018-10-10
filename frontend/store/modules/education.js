// initial state
// shape: [{ id, quantity }]
const state = {
  education: [],
  courses: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setEducation: (state, education) => {
    state.education = education
  },
  setCourses: (state, courses) => {
    state.courses = courses
  }
}

// actions
const actions = {
  async getEducation ({commit}) {
    const data = await this.$axios.$get(`education/?format=json`)
    commit('setEducation', data)
  },
  async getCourses ({commit}) {
    const data = await this.$axios.$get(`courses/?format=json`)
    commit('setCourses', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
