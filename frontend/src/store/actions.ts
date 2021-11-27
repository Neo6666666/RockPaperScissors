import { ActionTree, ActionContext } from 'vuex'
import axios from 'axios'

import router, { RouteNames } from '@/router'

import { State } from './state'
import { Mutations, Mutation } from './mutations'

export enum Action {
  initApp = 'initApp',
  login = 'login',
  register = 'register',
  logout = 'logout'
}

type AugmentedActionContext = {
  commit<K extends keyof Mutations>(
    key: K,
    payload?: Parameters<Mutations[K]>[1]
  ): ReturnType<Mutations[K]>
} & Omit<ActionContext<State, State>, 'commit'>

export interface Actions {
  [Action.initApp]({ state, commit, dispatch }: AugmentedActionContext): void
}

export const actions: ActionTree<State, State> & Actions = {
  [Action.initApp] () {
    console.log('app inited!')
  },

  async [Action.register] ({ commit }, user) {
    try {
      const { data } = await axios.post('http://localhost:8000/api/register/', user)

      commit(Mutation.SET_USER, data)
      router.push({ name: RouteNames.Home })
    } catch (error) {
      console.log(error)
    }
  },

  async [Action.login] ({ commit }, user) {
    try {
      const { data } = await axios.post('http://localhost:8000/api/login/', user)

      commit(Mutation.SET_USER, data)
      router.push({ name: RouteNames.Home })
    } catch (error) {
      console.log(error)
    }
  },

  async [Action.logout] ({ commit }) {
    try {
      commit(Mutation.CLEAR_STATE)
      router.push({ name: RouteNames.Login })
    } catch (error) {
      console.log(error)
    }
  },
}
