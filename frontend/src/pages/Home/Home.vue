<script setup lang="ts">
import Table from '@/components/Table';
import { onMounted } from '@vue/runtime-core';
import { ref, reactive } from '@vue/reactivity';
import { useStore } from 'vuex';
import WebSocketService from './Foo'

enum messageStatus {
  NEW_USER = 'NEW_USER',
  ADD_USERS = 'ADD_USERS',
  RM_USER = 'RM_USER'
}

const store = useStore()

const users = ref([]);
const data = reactive({ users });
let webSocketConnection = null;

onMounted(() => {
  init()
})

const inviteUser = (id: number) => webSocketConnection.emit({
  'content_type': 'INVITE_USER',
  'host_id': store.state.user.id,
  'guest_id': id
})

const init = () => {
  try {
    console.log('initConnection')

    webSocketConnection = new WebSocketService(`${store.state.user.id}`)

    webSocketConnection.onMessage((payload: any) => {
      console.log('123123123123', payload);

      if (payload.content_type === messageStatus.RM_USER) {
        data.users = data.users.filter(user => user.id !== payload.user.id)
      } else if (payload.content_type === messageStatus.ADD_USERS) {
        // store.commit('setUsers', payload.users)
        data.users = payload.users;
      } else {
        // store.commit('addUser', payload.user)
        data.users.push(payload.user);
      }
    })

    // store.subscribe((action: any) => {
    //   socketReducer(action, webSocketConnection)
    // })
  } catch (error) {
    console.log(error)
  }
}
</script>

<template>
  <div class="flex items-start justify-center min-h-screen">
      <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <Table v-if="data?.users?.length" :data="data.users" @onClick="inviteUser"></Table>
      </div>
  </div>
</template>
