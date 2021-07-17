<template>
  <div class="login">
    <SignComponent :title="formTitle" @formAction="submitForm"/>
  </div>
</template>

<script lang="ts">
import { useStore } from 'vuex';
import { defineComponent, Ref, ref } from 'vue';
import SignComponent  from "@/components/Sign.component.vue";
import { SignFormData } from "@/models/forms/SignFormData.interface";

export default defineComponent({
  name: 'Login',
  components:{
    SignComponent
  },
  setup() {
    const store = useStore()

    const formTitle: String = "Sign In";
    const submitForm = (e: SignFormData) => {
        console.log(e);
        
        store.dispatch('login', {
          username: e.username,
          password: e.password
          });
    }
    return {
      formTitle,
      submitForm
    };
  },
});
</script>
