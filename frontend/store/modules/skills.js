// initial state
// shape: [{ id, quantity }]
const state = {
  skills: [],
  skill_categories: [],
  skills_cat: []
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
  },
  setSkillCat: (state, skills_cat) => {
    state.skills_cat = skills_cat
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
  },
  async getSkillsCat ({commit}, url) {
    const data = await this.$axios.$get(`skills/search/${url}/?format=json`)
    commit('setSkillCat', data)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
