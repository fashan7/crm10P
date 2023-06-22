import  { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',
    state:() => ({
        user: {
            isAuthenticated: false,
            name: null,
            email: null,
            access: null,
            refresh: null
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true

                this.refreshToken()
                console.log('Initialized user', this.user)
            }
        },

        setToken(data) {
            console.log('setToken', data)
            this.user.access  = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            console.log('RemoveToken')

            this.user.access  = null
            this.user.refresh = null
            this.user.isAuthenticated = false
            this.user.name = false
            this.user.email = false
            

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
        },

        setUserInfo(user) {
            console.log('SetUserInfo', user)
            this.user.name = user.name
            this.user.email = user.email
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)

            console.log('User', this.user)
        },

        refreshToken() {
            axios.post('/api/user/refresh/', {
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