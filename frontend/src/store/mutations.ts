import { MutationTree } from 'vuex'
import { State } from './state'

export enum Mutation {
  INCREMENT = 'INCREMENT',
  SET_USER = 'SET_USER',
  CLEAR_STATE = 'CLEAR_STATE'
}

export type Mutations<S = State> = {
  [Mutation.INCREMENT](state: S, payload: number): void
}

export const mutations: MutationTree<State> & Mutations = {
  [Mutation.INCREMENT](state: State, payload: number = 1) {
    state.count += payload
  },

  [Mutation.SET_USER](state: State, payload) {
    state.user = payload
  },

  [Mutation.CLEAR_STATE](state: State) {
    state.user = {}
  },
}
