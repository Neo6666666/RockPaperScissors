import Api from '@/services/api'

interface IUser {
    username: string
    status: string
    id: string
}

const localUser: any = JSON.parse(localStorage.getItem('user') || 'false');

console.log(localUser);

export default {
    state: (): { user: IUser } => ({
        user: {
            username: "",
            status: "",
            id: ""
        }
    }),
    mutations: {
        set(state: any, payload: IUser) {
            if (!localUser || state.user.id) {
                localStorage.setItem('user', JSON.stringify(payload));
            }

            state.user = payload;
        }
    },
    getters: {
        loggedIn(state: any) {
            const user: IUser = localUser || state.user

            return user.id;
        }
    },
    actions: {
        async login({ commit }: any, body: any) {
            const { data } = await Api.createRequest('login', body);

            commit('set', data)
        },
        async register({ commit }: any, body: any) {
            const { data } = await Api.createRequest('register', body);

            commit('set', data)
        }
    }
}