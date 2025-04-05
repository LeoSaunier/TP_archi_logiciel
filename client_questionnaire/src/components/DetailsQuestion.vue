<script>
import { ref } from 'vue';

export default {
    props: {
        question: Object,
    },
    methods: {
        modify() {
            this.$emit('updateQuestion', this.question);
        }
    },
    emits: ['updateQuestion'],
}
</script>

<template>
    <div>
        <div v-if="this.question.questionType == 'open_question'">
            <div>
                <input type="text" v-model="this.question.title" placeholder="Question Title">
                <input type="text" v-model="this.question.reponse" placeholder="Question Description">
            </div>
        </div>
        <div v-else-if="this.question.questionType == 'simple_question'">
            <input type="text" v-model="question.title" placeholder="Question Title">
            <input type="number" v-model="question.reponse" placeholder="Question Description">
            <input type="text" v-model="question.proposition1" placeholder="Proposition 1">
            <input type="text" v-model="question.proposition2" placeholder="Proposition 2">
        </div>
        <button @click="modify">Modify</button>
    </div>
</template>