<script>
import { ref, watch } from 'vue';
import AllQuestion from './AllQuestion.vue';

export default {
    props: {
        questionnaire: Object,
        questions: Array
    },
    setup() {
        const selectedQuestionType = ref(null);
        const Q1selected = ref(false);
        const Q2selected = ref(false);
        const question = ref({ title: '', description: '', propositions: ['', ''] });

        watch(selectedQuestionType, (newValue) => {
            Q1selected.value = newValue === 'Q1';
            Q2selected.value = newValue === 'Q2';
        });

        return { selectedQuestionType, Q1selected, Q2selected, question };
    },
    components: {
        AllQuestion
    },
    methods: {
        deleteQuestionnaire() {
            this.$emit('deleteQuestion', this.questionnaire);
        },
        updateQuestionnaire() {
            this.$emit('updateQuestionnaire', this.questionnaire);
        },
        addQuestionOuverte() {
            this.$emit('addQuestionOuverte', { ...this.question, type: 'Q1' });
        },
        addQuestionSimple() {
            this.$emit('addQuestionSimple', { ...this.question, type: 'Q2' });
        }
    },
    emits: ['deleteQuestion', 'updateQuestionnaire', 'addQuestionOuverte', 'addQuestionSimple']
};
</script>

<template>
    <div>
        <div>
            <input type="text" v-model="questionnaire.name" placeholder="Questionnaire Name">
            <button @click="updateQuestionnaire">Update</button>
        </div> 
        <AllQuestion
            :questions="questions"
            @deleteQuestion="deleteQuestionnaire"
        >
        </AllQuestion>
        <div>
            <fieldset>
                <legend>Type de question :</legend>
                <div>
                    <input type="radio" id="Q1" value="Q1" v-model="selectedQuestionType" />
                    <label for="Q1">Question ouverte</label>
                </div>
                <div>
                    <input type="radio" id="Q2" value="Q2" v-model="selectedQuestionType" />
                    <label for="Q2">Question simple</label>
                </div>
            </fieldset>

            <div v-if="Q1selected">
                <label>
                    <input type="text" v-model="question.title" placeholder="Nom de la question">
                    <input type="text" v-model="question.awnser" placeholder="Réponse">
                </label>
                <button class="btn btn-add" @click="addQuestionOuverte">Ajouter</button>
            </div>
            
            <div v-if="Q2selected">
                <label>
                    <input type="text" v-model="question.title" placeholder="Nom de la question">
                    <input type="text" v-model="question.awnser" placeholder="Réponse">
                    <input type="text" v-model="question.propositions[0]" placeholder="Proposition 1">
                    <input type="text" v-model="question.propositions[1]" placeholder="Proposition 2">
                </label>
                <button class="btn btn-add" @click="addQuestionSimple">Ajouter</button>
            </div>
        </div>
    </div>
</template>
