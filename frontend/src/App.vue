<script setup lang="ts">
import { onBeforeMount } from "vue";
import { RouterView } from "vue-router";
import { useUserStore } from "./stores/user";
import axios from "axios";
import router from "./router";

const userStore = useUserStore();
onBeforeMount(() => {
   userStore.initStore();
   const token = userStore.user.access;
   userStore.removeToken() 

   console.log('dads')
   console.log(userStore.user.isAuthenticated)
   if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer "+token;
      
   } else {
      axios.defaults.headers.common["Authorization"] = "";
   }

   if (userStore.user.isAuthenticated){ 
      console.log("going dashboad B4Mounted");
      router.push("/dashboard");
   } else {
      console.log("going login B4Mounted");
      router.push("/login");
   }
});
onMounted(() => {
   if (userStore.user.isAuthenticated){ 
      console.log("going dashboadrd after mounted");
      router.push("/dashboard");
   } else {
      console.log("going login after mounted");
      router.push("/login");
   }
  
}); 
</script>

<template > 
   <RouterView />
</template>