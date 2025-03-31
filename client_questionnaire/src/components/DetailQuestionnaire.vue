<script>
import { ref } from 'vue';
export default {
    setup() {
        const Q1selected = ref(false);
        const Q2selected = ref(false);
        return { Q1selected, Q2selected };
    },
    props: {
        questionnaire: Object
    },
    methods: {
        selectQuestionnaire() {
            this.$emit('selectQuestion', this.question);
        },
        deleteQuestionnaire() {
            this.$emit('deleteQuestion', this.question);
        }
    },
    emits: ['selectQuestion', 'deleteQuestion']
};
</script>


<template>
    <div>
        <div>
            <input type="text" v-model="questionnaire.name" placeholder="Questionnaire Name">
        </div> 
        <div class="card" v-for = "question in questionnaire.questions">
            <button @click="selectQuestion">Select</button>
            <button @click="deleteQuestion">Delete</button>
        </div>
        <div>
            <input type="select" v-model="questionnaire.name" placeholder="Questionnaire Name">

            <div v-if ="Q1selected">
                <label>
                    <input type="text" v-model="questionnaire.title" placeholder="Nom de la question">
                    <input type="text" v-model="questionnaire.description" placeholder="Description du questionnaire">
                </label>
                <button class="btn btn-add" @click="addQuestionnaire">Ajouter</button>
            </div>
            <div v-if ="Q2selected">
                <label>
                    <input type="text" v-model="questionnaire.title" placeholder="Nom de la question">
                    <input type="text" v-model="questionnaire.description" placeholder="Description du questionnaire">
                </label>
                <button class="btn btn-add" @click="addQuestionnaire">Ajouter</button>
            </div>
        </div>

    </div>
</template>