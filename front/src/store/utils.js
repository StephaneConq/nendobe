export default {
    namespaced: true,
    state: () => ({
        globalLoading: false
    }),
    mutations: {
        setGlobalLoading(state, loading) {
            state.globalLoading = loading;
        }
    },
    getters: {
        globalLoading( state ) {
            return state?.globalLoading;
        }
    }
}