<script setup lang="ts">
import { ref } from '@vue/reactivity';
import { useStore } from 'vuex';

import passwordSvg from '@/assets/icons/password.svg'
import mailSvg from '@/assets/icons/mail.svg'

import { Action } from '@/store'
import * as Form from '@/components/Form'

const store = useStore()

const username = ref('');
const password = ref('');

const submit = () => {
  store.dispatch(Action.register, {
    username: username.value,
    password: password.value
  })
}
</script>

<template>
  <div class="container h-screen flex justify-center items-center">
    <div class="flex flex-col justify-center">
      <Form.Container
        title="Register."
        @submit="submit"
      >
        <template v-slot:fields>
          <div class="flex flex-col pt-4">
            <Form.Input
              v-model="username"
              :icon="mailSvg"
              placeholder="Username"
              type="name"
            />
          </div>

          <div class="flex flex-col pt-4 mb-12">
            <Form.Input
              v-model="password"
              :icon="passwordSvg"
              placeholder="Password"
              type="password"
            />
          </div>
        </template>

        <template v-slot:actions>
          <button
            type="submit"
            class="px-4 py-2 text-base font-semibold text-center text-white transition duration-200 ease-in bg-black shadow-md hover:text-black hover:bg-white focus:outline-none focus:ring-2"
          >
            <span class="w-full">Submit</span>
          </button>
        </template>

        <template v-slot:footer>
          <div class="pt-12 pb-12 text-center">
            <p>
              Have account?
              <router-link :to="{ name: 'Login' }" class="font-semibold underline">Login here.</router-link>
            </p>
          </div>
        </template>
      </Form.Container>
    </div>
  </div>
</template>
