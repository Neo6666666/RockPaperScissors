<template>
  <div class="form-input">
    <input
      :value="modelValue"
      @input="handleInput"
      :name="inputName"
      :type="type"
      class="form-input__control"
    />
    <label class="form-input__label" for="username">
      {{ label }}
    </label>
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
    type: String,
    inputName: String,
    modelValue: String,
  },
  emits: ["update:modelValue"],
  setup(props, { emit }) {
    const handleInput = (e: Event) => {
      const target = e.target as HTMLInputElement;

      console.log(e);

      emit("update:modelValue", target.value);
    };

    return { handleInput };
  },
});
</script>

<style>
.form-input {
  display: flex;
  align-items: center;
  position: relative;
  margin-bottom: 26px;
  width: 100%;
  height: 20px;
}

.form-input__label {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 10px;
  transition: all 0.3s ease-out;
}

.form-input__control {
  width: 100%;
  height: 100%;
  border: none;
  border-bottom: 1px solid #cdcdcd;
  border-radius: 10px;
}

.form-input__control:focus + label {
  top: -24px;
}

/* .form-input__control:focus ~ label {
  top: 10px;
} */
</style>
