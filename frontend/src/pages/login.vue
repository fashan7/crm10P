<script setup lang="ts">
import axios from 'axios';
import { ref, Ref } from 'vue';
import { useUserStore } from '@/stores/user';
import logo from '@images/logo.svg?raw'
import router from '@/router';

const form = ref({
  email:'',
  password:'',
  remember:false
})

const userStore = useUserStore();
const errors = ref<string[]>([]);
const login = async () => {
  errors.value = [];

  if (form.value.email === '') {
    errors.value.push('Your email is missing');
  }

  if (form.value.password === '') {
    errors.value.push('Your password is missing');
  }

  if (errors.value.length === 0) {
    try {
      const response = await axios.post('/api/login/', form.value);
      userStore.setToken(response.data);
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
    } catch (error) {
      console.log('error', error);
      errors.value.push('The email or password is incorrect! Or the user is not activated!');
    }

    if (errors.value.length === 0) {
      try {
        const response = await axios.get('/api/me/');
        userStore.setUserInfo(response.data);
        router.push('/');
      } catch (error) {
        console.log('error', error);
      }
    }
  }
}

const isPasswordVisible = ref(false)
</script>

<template>
  <div class="auth-wrapper d-flex align-center justify-center pa-4">
    <VCard
      class="auth-card pa-4 pt-7"
      max-width="448"
    >
      <VCardItem class="justify-center">
        <template #prepend>
          <div class="d-flex">
            <div
              class="d-flex text-primary"
              v-html="logo"
            />
          </div>
        </template>

        <VCardTitle class="text-2xl font-weight-bold">
          sneat
        </VCardTitle>
      </VCardItem>

      <VCardText class="pt-2">
        <h5 class="text-h5 mb-1">
          Welcome to sneat! 👋🏻
        </h5>
        <p class="mb-0">
          Please sign-in to your account and start the adventure
        </p>
      </VCardText>

      <VCardText>
        <VForm novalidate @submit.prevent="login">
          <VRow>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                v-model="form.email"
                autofocus
                placeholder="johndoe@email.com"
                label="Email"
                type="email"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextField
                v-model="form.password"
                label="Password"
                placeholder="············"
                :type="isPasswordVisible ? 'text' : 'password'"
                :append-inner-icon="isPasswordVisible ? 'bx-hide' : 'bx-show'"
                @click:append-inner="isPasswordVisible = !isPasswordVisible"
              />

              <!-- remember me checkbox -->
              <div class="d-flex align-center justify-space-between flex-wrap mt-1 mb-4">
                <VCheckbox
                  v-model="form.remember"
                  label="Remember me"
                />

                <RouterLink
                  class="text-primary ms-2 mb-1"
                  to="javascript:void(0)"
                >
                  Forgot Password?
                </RouterLink>
              </div>

              <!-- login button -->
              <VBtn
                block
                type="submit"
              >
                Login
              </VBtn>
            </VCol>

            <!-- create account -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>New on our platform?</span>
              <RouterLink
                class="text-primary ms-2"
                to="/register"
              >
                Create an account
              </RouterLink>
            </VCol>
          </VRow>
        </VForm>
      </VCardText>
    </VCard>
  </div>
</template>

<style lang="scss">
@use "@core/scss/template/pages/page-auth.scss";
</style>
