import { generateName } from '../utils';

export default {
    namespaced: true,
    state: () => {
        return {
            currentNendoroids: [],
            prices: {},
            selectedNendoroid: null
        }
    },
    mutations: {
        setCurrentNendoroids(state, nendoroids) {
            state.currentNendoroids = [...nendoroids];
        },
        setPrices(state, prices) {
            if (prices === null) {
                state.prices = {};
            }
            state.prices = { ...state.prices, ...prices };
        },
        setSelectedNendoroid(state, nendoroid) {
            state.selectedNendoroid = nendoroid;
        }
    },
    getters: {
        currentNendoroids({ state }) {
            return state.currentNendoroids;
        },
        selectedNendoroid({state}) {
            return state.selectedNendoroid;
        }
    },
    actions: {
        getNendoroidById( { commit }, nendoroidId) {
            commit('utilsStore/setGlobalLoading', true, {root: true});
            commit('nendoroidsStore/setCurrentNendoroids', []);
            commit('nendoroidsStore/setPrices', null);
            commit('nendoroidsStore/setSelectedNendoroid');

            fetch(`${import.meta.env.VITE_API_URL}/nendoroids/${nendoroidId}`).then(response => {
                response.json().then(nendoroids => {
                    commit('nendoroidsStore/setCurrentNendoroids', nendoroids);
                    const promises = [];

                    nendoroids.forEach(nendoroid => {
                        promises.push(dispatch('nendoroidsStore/updatePrices', nendoroid.id));
                    });

                    Promise.all(promises).then(() => {
                        commit('utilsStore/setGlobalLoading', false, {root: true});
                    });
                });
            })
        },
        updatePrices({ state, commit }, nendoroidId) {
            return new Promise(resolve => {

                const nendoroid = state.currentNendoroids.find(n => n.id === nendoroidId);
                
                if (nendoroid) {

                    const promises = [];
                    const name = generateName(nendoroid);

                    ['ebay', 'ninnin', 'playasia'].forEach(source => {
                        promises.push(fetch(`${import.meta.env.VITE_API_URL}/prices?name=${name}&source=${source}`));
                    });

                    Promise.all(promises).then(responses => {
                        const pricesPromise = [];
                        responses.forEach(r => pricesPromise.push(r.json()));

                        Promise.all(pricesPromise).then(prices => {
                            commit('setPrices', {
                                [nendoroidId]: {
                                    ebay: prices[0],
                                    ninnin: prices[1],
                                    playasia: prices[2]
                                }
                            });
                            resolve(prices);
                        }); 
                    });

                } else {
                    console.log('nendoroid not found, was looking in', state.currentNendoroids);
                }
            });

        }
    }
}