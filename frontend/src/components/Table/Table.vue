<script setup lang="ts">
const props = defineProps<{
  data: Record<string, unknown>
}>()

const emit = defineEmits<{
  (event: 'onClick', id: number): void
}>()

const onClick = (id: number) => emit('onClick', id);
</script>

<template>
  <table class="table border-separate space-y-6 text-sm">
    <thead class="bg-gray-100 text-gray-400">
      <tr>
        <th class="p-3">Name</th>
        <th class="p-3">Status</th>
        <th class="p-3">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr class="bg-gray-100" v-for="(user, i) in props.data" :key="i">
        <td class="p-3">
          <div class="flex align-items-center">
            <img class="rounded-full h-12 w-12 object-cover" src="https://images.unsplash.com/photo-1613588718956-c2e80305bf61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80" alt="unsplash image">

            <div class="ml-6 items-center flex">
              <div class="text-gray-500">{{user.username}}</div>
            </div>
          </div>
        </td>

        <td class="p-3">
          <span class="bg-green-400 text-gray-50 rounded-md px-2">{{user.status}}</span>
        </td>

        <td class="p-3 ">
          <button @click="() => onClick(user.id)">
            <span class="text-base text-blue-400">Invite</span>
          </button>
        </td>
      </tr>
      <!-- <tr class="bg-gray-300">
        <td class="p-3">
          <div class="flex align-items-center">
            <img class="rounded-full h-12 w-12   object-cover" src="https://images.unsplash.com/photo-1423784346385-c1d4dac9893a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80" alt="unsplash image">
            <div class="ml-3">
              <div class="">Realme</div>
              <div class="text-gray-500">mail@rgmail.com</div>
            </div>
          </div>
        </td>
        <td class="p-3">
          Technology
        </td>
        <td class="p-3 font-bold">
          200.00$
        </td>
        <td class="p-3">
          <span class="bg-red-400 text-gray-50 rounded-md px-2">no stock</span>
        </td>
        <td class="p-3">
          <a href="#" class="text-gray-400 hover:text-gray-100  mr-2">
            <i class="material-icons-outlined text-base">visibility</i>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-100 mx-2">
            <i class="material-icons-outlined text-base">edit</i>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-100 ml-2">
            <i class="material-icons-round text-base">delete_outline</i>
          </a>
        </td>
      </tr>
      <tr class="bg-gray-300">
        <td class="p-3">
          <div class="flex align-items-center">
            <img class="rounded-full h-12 w-12   object-cover" src="https://images.unsplash.com/photo-1600856209923-34372e319a5d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2135&q=80" alt="unsplash image">
            <div class="ml-3">
              <div class="">Samsung</div>
              <div class="text-gray-500">mail@rgmail.com</div>
            </div>
          </div>
        </td>
        <td class="p-3">
          Technology
        </td>
        <td class="p-3 font-bold">
          200.00$
        </td>
        <td class="p-3">
          <span class="bg-yellow-400 text-gray-50  rounded-md px-2">start sale</span>
        </td>
        <td class="p-3">
          <a href="#" class="text-gray-400 hover:text-gray-100 mr-2">
            <i class="material-icons-outlined text-base">visibility</i>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-100 mx-2">
            <i class="material-icons-outlined text-base">edit</i>
          </a>
          <a href="#" class="text-gray-400 hover:text-gray-100 ml-2">
            <i class="material-icons-round text-base">delete_outline</i>
          </a>
        </td>
      </tr> -->
    </tbody>
  </table>
</template>

<style scoped>
.table {
  border-spacing: 0 15px;
}

i {
  font-size: 1rem !important;
}

.table tr {
  border-radius: 20px;
}

tr td:nth-child(n+3),
tr th:nth-child(n+3) {
  border-radius: 0 .625rem .625rem 0;
}

tr td:nth-child(1),
tr th:nth-child(1) {
  border-radius: .625rem 0 0 .625rem;
}
</style>