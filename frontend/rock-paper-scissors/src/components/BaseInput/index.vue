<template>
  <div class="form__control form-input">
    <label class="form-input__label" for="username">
      {{ label }}
    </label>
    <input
      @input="handleInput"
      :value="value"
      :name="inputName"
      class="form-input__main"
      type="text"
    />
  </div>
</template>

<script lang="ts">
import { reactive, defineComponent } from "vue";

// type TState = { value: string };
// type TSetupState = { state: TState; handleChange: () => void };
// type TProps = {
//   label: string;
//   inputName: string;
//   value: string;
// };

export default defineComponent({
  name: "BaseInput",
  props: {
    label: String,
    inputName: String,
    value: String,
  },
  setup(props, { emit }) {
    const handleInput = (e: Event) => {
      const target = e.target as HTMLInputElement;

      emit("handle-input", target.value);
    };

    return { handleInput };
  },
});
</script>

<style></style>
