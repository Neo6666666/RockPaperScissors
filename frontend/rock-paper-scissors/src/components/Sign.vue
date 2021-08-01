<template>
  <div class="sign-form-container">
    <h3>{{ title }}</h3>
    <form @submit.prevent="submitForm" class="sign-form">
      <div class="form-control">
        <label for="username">Username</label>
        <input v-model="state.username" type="text" name="username" />
      </div>
      <div class="form-control">
        <label for="password">Password</label>
        <input v-model="state.password" type="password" name="password" />
      </div>
      <div class="form-control">
        <input type="submit" value="Submit" />
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  props: {
    title: String,
  },
  setup(props, { emit }) {
    const state: Record<string, string> = reactive({
      username: "",
      password: "",
    });

    const submitForm = () => {
      emit("formAction", {
        username: state.username,
        password: state.password,
      });
    };
    return {
      state,

      submitForm,
    };
  },
});
</script>

<style src=""></style>
