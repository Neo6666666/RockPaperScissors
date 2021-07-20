<template>
  <div class="sign-form-container">
    <h3>{{ title }}</h3>
    <form @submit="submitForm" class="sign-form">
      <div class="form-control">
        <label for="username">Username</label>
        <input v-model="username" type="text" name="username" />
      </div>
      <div class="form-control">
        <label for="password">Password</label>
        <input v-model="password" type="password" name="password" />
      </div>
      <div class="form-control">
        <input type="submit" value="Submit" />
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, Ref } from "vue";

export default defineComponent({
  props: {
    title: String,
  },
  setup(props, { emit }) {
    const username: Ref<string> = ref("");
    const password: Ref<string> = ref("");
    const submitForm = (e: Event) => {
      e.preventDefault();
      emit("formAction", {
        username: username.value,
        password: password.value,
      });
    };
    return {
      username,
      password,

      submitForm,
    };
  },
});
</script>

<style>
.sign-form-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3));
  width: 380px;
  padding: 50px 30px;
  border-radius: 10px;
  box-shadow: 7px 7px 60px black;
}
h3 {
  font-size: 2em;
  text-align: center;
  margin-bottom: 2em;
}
.form-control input {
  width: 100%;
  display: block;
  padding: 10px;
  color: #222;
  border: none;
  outline: none;
  margin: 1em 0em;
}
.form-control input[type="submit"] {
  background: rgb(34, 113, 216);
  color: white;
  text-transform: uppercase;
  font-size: 1.2em;
  opacity: 0.8;
}
</style>
