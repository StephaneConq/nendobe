export default {
    namespaced: true,
    state: () => ({
        globalLoading: false,
        displaySnackbar: false,
        snackbarInfo: {}
    }),
    mutations: {
        setGlobalLoading(state, loading) {
            state.globalLoading = loading;
        },
        setSnackbar(state, payload) {
            state.displaySnackbar = payload.displaySnackbar;
            state.snackbarInfo = payload.snackbarInfo;
        }
    },
    getters: {
        globalLoading( state ) {
            return state?.globalLoading;
        }
    }
}