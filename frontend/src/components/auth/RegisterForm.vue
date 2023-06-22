<template>
    <form v-on:submit.prevent="signup">
    <v-row class="d-flex mb-3">
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Name</v-label>
            <v-text-field v-model="form.name" variant="outlined" hide-details color="primary"></v-text-field>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Email Address</v-label>
            <v-text-field v-model="form.email" variant="outlined" type="email" hide-details color="primary"></v-text-field>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Password</v-label>
            <v-text-field v-model="form.password1" variant="outlined" type="password"  hide-details color="primary"></v-text-field>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-bold mb-1">Retype Password</v-label>
            <v-text-field v-model="form.password2" variant="outlined" type="password"  hide-details color="primary"></v-text-field>
        </v-col>
        <v-col cols="12" >
            <v-btn color="primary" size="large" block   flat type="submit" v-on:click="signup">Sign up</v-btn>
        </v-col>
    </v-row>
    <v-row class="d-flex mb-3">
        <template v-if="errors">
            <v-col cols="12">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </v-col>
        </template>
    </v-row>

</form>
</template>
<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';

interface Form {
  email: string;
  name: string;
  password1: string;
  password2: string;
}

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
      alert('Hii');
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
            console.log('error', error);
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
