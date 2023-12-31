import  { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',
    state:() => ({
        user: {
            isAuthenticated: false,
            name: null as string | null,
            email: null as string | null,
            access: null as string | null,
            refresh: null as string | null
        }
    }),

    actions: {
        initStore() {
            console.log('initStore');
            if (localStorage.getItem('user.access')) {
                console.log('User has access');
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true

                this.refreshToken()
                console.log('Initialized user', this.user)
            }
        },

        setToken(data:any) {
            console.log('setToken', data)
            this.user.access  = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh);

            console.log('user.access ',localStorage.getItem('user.access'));
        },

        removeToken() {
            console.log('RemoveToken')

            this.user.access  = null
            this.user.refresh = null
            this.user.isAuthenticated = false
            this.user.name = null
            this.user.email = null
            

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
        },

        setUserInfo(user:any) {
            console.log('SetUserInfo', user)
            this.user.name = user.name
            this.user.email = user.email
            localStorage.setItem('user.name', user.name)
            localStorage.setItem('user.email', user.email)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    axios.defaults.headers.common["Authorization"] = "Bearer "+ response.data.access 
                })
                .catch((error) => {
                    console.log(error)
                    this.removeToken()
                })
        }
    }
})