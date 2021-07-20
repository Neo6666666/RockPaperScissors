import { createStore } from "vuex";
import user from "./user";

export default createStore({
  strict: process.env.NODE_ENV !== "production",
  modules: {
    user,
  },
});
