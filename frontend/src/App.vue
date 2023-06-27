<script setup lang="ts">
import { onBeforeMount } from "vue";
import { RouterView } from "vue-router";
import { useUserStore } from "./stores/user";
import axios from "axios";


onBeforeMount(() => {
   const userStore = useUserStore();
   userStore.initStore();
   const token = userStore.user.access;
   // userStore.removeToken()
   if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer "+token;
   } else {
      axios.defaults.headers.common["Authorization"] = "";
   }
}); 
</script>

<template>
   <RouterView />
</template>