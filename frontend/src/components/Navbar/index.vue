<script setup lang="ts">
import { useStore } from 'vuex'
import { computed } from '@vue/reactivity'

import { RouteNames } from '@/router'
import { Action } from '@/store'

const store = useStore()
const isLoggedIn = computed(() => store.getters.isLoggedIn)
const defaultClasses = 'px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:text-gray-800 dark:hover:text-white cursor-pointer'
const activeClasses = 'text-gray-800 dark:text-white hover:text-gray-800 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium'

const links = computed(() => [
  {
    label: 'Home',
    to: RouteNames.Home,
    visible: isLoggedIn.value,
  },
  {
    label: 'Logout',
    visible: isLoggedIn.value,
    action: () => store.dispatch(Action.logout),
  },
  {
    label: 'Login',
    to: RouteNames.Login,
    visible: !isLoggedIn.value,
  },
  {
    label: 'Register',
    to: RouteNames.Register,
    visible: !isLoggedIn.value,
  }
]);
</script>

<template>
  <div>
      <nav class="bg-white dark:bg-gray-800  shadow ">
          <div class="max-w-7xl mx-auto px-8">
              <div class="flex items-center justify-between h-16">
                  <div class="w-full justify-between flex items-center">

                      <a class="flex-shrink-0" :to="{ name: 'Home' }">
                        {{isLoggedIn}}
                      </a>

                      <div class="hidden md:block">
                          <div class="ml-10 flex items-baseline space-x-4">
                            <template v-for="navLink in links" :key="navLink.label">

                              <router-link
                                v-if="(navLink.visible && !navLink.action)"
                                :to="{ name: navLink.to }"
                                custom
                                v-slot="{ href, navigate, isActive }"
                              >
                                <a
                                  :class="isActive ? activeClasses : defaultClasses"
                                  :href="href"
                                  @click="navigate"
                                >
                                  {{ navLink.label }}
                                </a>
                              </router-link>

                              <a
                                v-else-if="navLink.visible"
                                :class="defaultClasses"
                                @click="navLink.action"
                              >
                                {{ navLink.label }}
                              </a>

                            </template>
                          </div>
                      </div>
                  </div>

                  <div class="block">
                      <div class="ml-4 flex items-center md:ml-6"></div>
                  </div>

                  <div class="-mr-2 flex md:hidden">
                      <button class="text-gray-800 dark:text-white hover:text-gray-300 inline-flex items-center justify-center p-2 rounded-md focus:outline-none">
                          <svg width="20" height="20" fill="currentColor" class="h-8 w-8" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                              <path d="M1664 1344v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45z"></path>
                          </svg>
                      </button>
                  </div>

              </div>
          </div>

          <div class="md:hidden">
              <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                  <a class="text-gray-300 hover:text-gray-800 dark:hover:text-white block px-3 py-2 rounded-md text-base font-medium" href="/#">
                      Home
                  </a>
              </div>
          </div>

      </nav>
  </div>
</template>
