<template>
    <v-snackbar v-model="display">
        {{ info.text }}

        <template v-slot:actions>
            <v-btn color="pink" variant="text" @click="close">
                Fermer
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script>
import {useStore} from 'vuex';
import {computed} from 'vue';

export default {
    setup() {
        const store = useStore();

        const close = () => {
            store.commit('utilsStore/setSnackbar', {
                displaySnackbar: false,
                snackbarInfo: {}
            });
        };

        const info = computed(() => store.state.utilsStore.snackbarInfo);
        const display = computed(() => store.state.utilsStore.displaySnackbar);

        return {
            info,
            display,
            close
        }
    }
}

</script>

<style></style>