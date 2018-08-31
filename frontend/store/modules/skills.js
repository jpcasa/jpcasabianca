// initial state
// shape: [{ id, quantity }]
const state = {
  skills: [],
  skill_categories: []
}

// getters
const getters = {}

// mutations
const mutations = {
  setSkills: (state, skills) => {
    state.skills = skills
  },
  setSkillCategories: (state, skill_categories) => {
    state.skill_categories = skill_categories
  }
}

// actions
const actions = {
  async getSkills ({commit}) {
    const data = await this.$axios.$get(`skills/?format=json`)
    commit('setSkills', data)
  },
  async getSkillCategories ({commit}) {
    const data = await this.$axios.$get(`skill-categories/?format=json`)
    commit('setSkillCategories', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
