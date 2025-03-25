<script>
export default {
    props: {
        questionnaire: Object
    },
    methods: {
        selectQuestionnaire() {
            this.$emit('selectQuestionnaire', this.questionnaire);
        },
        deleteQuestionnaire() {
            this.$emit('deleteQuestionnaire', this.questionnaire);
        }
    },
    emits: ['selectQuestionnaire', 'deleteQuestionnaire']
};
</script>


<template>
    <div class="card">
        <h3>{{ questionnaire.name }}</h3>
        <button @click="selectQuestionnaire">Select</button>
        <button @click="deleteQuestionnaire">Delete</button>
    </div>
</template>