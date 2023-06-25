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
          Adventure starts here 🚀
        </h5>
        <p class="mb-0">
          Make your app management easy and fun!
        </p>
      </VCardText>

      <VCardText>
        <VForm novalidate @submit.prevent="signup">
          <VRow>
            <!-- Username -->
            <VCol cols="12">
              <VTextField
                v-model="form.name"
                autofocus
                label="Username"
                placeholder="Johndoe"
              />
            </VCol>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                v-model="form.email"
                label="Email"
                placeholder="johndoe@email.com"
                type="email"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextField
                v-model="form.password1"
                label="Password"
                placeholder="············"
                :type="isPassword1Visible ? 'text' : 'password'"
                :append-inner-icon="isPassword1Visible ? 'bx-hide' : 'bx-show'"
                @click:append-inner="isPassword1Visible = !isPassword1Visible"
              />
            </VCol>

            <VCol cols="12">
              <VTextField
                v-model="form.password2"
                label="Confrim Password"
                placeholder="············"
                :type="isPassword2Visible ? 'text' : 'password'"
                :append-inner-icon="isPassword2Visible ? 'bx-hide' : 'bx-show'"
                @click:append-inner="isPassword2Visible = !isPassword2Visible"
              />
            </VCol>

            <VCol cols="12">
              <VBtn
                block
                type="submit"
              >
                Sign up
              </VBtn>
            </VCol>

            <!-- login instead -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>Already have an account?</span>
              <RouterLink
                class="text-primary ms-2"
                to="/login"
              >
                Sign in instead
              </RouterLink>
            </VCol>

            <VCol
              cols="12"
              class="d-flex align-center"
            >
              <VDivider />
              <span class="mx-4">or</span>
              <VDivider />
            </VCol>

            <!-- auth providers -->
            <VCol
              cols="12"
              class="text-center"
            >
              <AuthProvider />
            </VCol>
          </VRow>
        </VForm>
        <VRow>
          <template v-if="errors">
            <VCol cols="12">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </VCol>
          </template>
        </VRow>
      </VCardText>
    </VCard>
  </div>
</template>

<style lang="scss">
@use "@core/scss/template/pages/page-auth.scss";
</style>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';

import AuthProvider from '@/views/pages/authentication/AuthProvider.vue'
import logo from '@images/logo.svg?raw'

interface Form {
  email: string;
  name: string;
  password1: string;
  password2: string;
}


const isPassword1Visible = ref(false);
const isPassword2Visible = ref(false);

export default {
  setup() {
    const form: Form = ref({
      email: '',
      name: '',
      password1: '',
      password2: '',
    });

    const errors: string[] = ref([]);

    const signup = () => {
      errors.value = [];

      if (form.value.name === '') {
        errors.value.push('Your name is missing');
      }

      if (form.value.email === '') {
        errors.value.push('Your email is missing');
      }

      if (form.value.password1 === '') {
        errors.value.push('Your password is missing');
      }

      if (form.value.password1 !== form.value.password2) {
        errors.value.push('The password does not match');
      }

      if (errors.value.length === 0) {
        axios
          .post('/api/signup/', form.value)
          .then((response) => {
            alert("Ress"+response)
            if (response.data.message === 'success') {
              alert('User registered');
              form.value.email = '';
              form.value.name = '';
              form.value.password1 = '';
              form.value.password2 = '';
            } else {
              alert('Something went wrong :(');
            }
          })
          .catch((error) => {
            alert(error)
            if (error.response) {
              // The request was made and the server responded with a status code
              console.error('Response Error:', error.response.data);
              console.error('Response Status:', error.response.status);
              console.error('Response Headers:', error.response.headers);
            } else if (error.request) {
              // The request was made but no response was received
              console.error('Request Error:', error.request);
            } else {
              // Other errors
              console.error('Error:', error.message);
            }
          });
      }
    };

    return {
      form,
      errors,
      signup,
    };
  },
};
</script>
