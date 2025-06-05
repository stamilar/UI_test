import streamlit as st
import datetime
import json

st.set_page_config(page_title="Proposal Deal Information Form", layout="wide")
st.title("Proposal Deal Information Questions")
st.markdown("Please answer the following questions:")

with st.form("proposal_form"):
        client_name = st.text_input("Client or Prospect Company FULL Name")
        proactive_support = st.text_input("Are you seeking support for an RFP or Proactive Proposal?")
        business_type = st.text_input("New Business or Renewal")
        is_global = st.text_input("Is this prospect in LinkedIn customer under entire contract")
        deal_deadline = st.date_input("Due date (10 business day minimum)")

        first_draft_due = st.date_input("First Draft Due Date")
        current_sku = st.text_input("Current SKU (if applicable)")
        proposed_sku = st.text_input("Proposed SKU")
        current_sales_package = st.text_input("Current Sales Package (if applicable)")
        proposed_package = st.text_input("Proposed Sales Package")
        adoption_stage = st.text_input("Current Adoption / Usage of Seats (eg. High, XX out of XX seats)")
        current_seats = st.text_input("Current No. of Seats")
        proposed_seats = st.text_input("Proposed No. of Seats")

        strategy_context = st.text_area("Strategy - Current State(At what stage is this opportunity? What commercial conversations have been held so far? What were the reactions and what upcoming meetings are lined up? - Do you have a live audience with the sponsor / all decision-makers?)")
        value_prop = st.text_area("Value Proposition(How are we going to win this and achieve buy-in for your recommended option? We like to align to the top 3 value propositions that would drive the narrative and strategy of this proposal.)")
        strategy_delivery = st.text_area("Strategy - Delivery of the ProposalDo you envision you will need support for a PowerPoint proposal that will be shared Live or are you looking for a leave-behind Proposal Document that can be shared internally with stakeholders? What help do you need from our team to make this successful?)")
        challenges = st.text_area("Challenges, Recommendations & Features(Are there any Customer Challenges / Problem statements that Sales Navigator Can Help With? )")
        insights_needs = st.text_area("Insights & Data (Do we have verified past usage insights from an SVR on Merlin? If not, will you be requesting some custom insights to be generated for this opportunity? By when do you expect to have that?)")
        additional_notes = st.text_area("Additional Things to note About this Opportunity (optional)")
        
        proposal_format = st.text_input("Proposed Proposal Format")
        proposal_length = st.text_input("Proposed Proposal Length (Page / Slides)")
        pricing_details = st.text_area("Investment Summary / Pricing Section Details :(Could you share the approved pricing? - Are we comparing pricing and giving the customer multiple options with one recommended option? - Is the pricing final? - Who will own the pricing section?):")
        customer_success = st.text_area("Implmentation & Customer Success (Partnering for Success) Section (Is there something we want to particularly highlight in the after-sale support services we will provide for this customer? - Will they qualify for a higher service package with your new proposal?)")
        service_packages = st.text_area("Service Packages Section (What would you like to see in the proposal? Only the Qualified Service Package vs Full Menu of Service Packages))")
        appendix = st.text_area("Appendix Section (Would this customer see value in seeing an appendix section with a short product overview, new AI features, The power of LinkedIn Data, and a nice graphic with a quote/testimonial from a customer?)")
        case_study = st.text_area("Case Study Section(Do you think a case study will add value to this proposal? If yes, what kind of case study should we add? Do we want one that highlights something specific that was achieved or one from a customer in a particular industry?)")
        graphics = st.text_area("Graphics & Images (Do you have any suggestions or recommendations on any graphic / image that would add value to this proposal?)")
        customer_name = st.text_area("Customer Name in Proposal(If a short form or variation of full legal name is preferred)")
        Proposal_Scenario = st.text_area("Proposal Scenario")
        unique_aspects = st.text_area("Unique Aspects of this Proposal (What is unique about this proposal?)")
        internal_challenges = st.text_area("Internal Challenges for this Proposal(eg. Justifying price increase, low adoption, customer feels price is too high, customer undergoing budget cuts, etc.)")
        start_date = st.date_input("Date Customer Started Using Sales Navigator")
        roles = st.text_area("Name of Roles within Customer's Org that are using Sales Navigator")
        competitors= st.text_area("Competitors(Are we competing against another company? If yes, who are they and what features are we competing with them on?)")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Proposal Deal Information submitted successfully!")
            st.balloons()
            form_data = {
                "Client Name": client_name,
                "RFP or Proactive": proactive_support,
                "Business Type": business_type,
                "Is Global": is_global,
                "Deal Deadline": str(deal_deadline),
                "First Draft Due": str(first_draft_due),
                "Current SKU": current_sku,
                "Proposed SKU": proposed_sku,
                "Current Sales Package": current_sales_package,
                "Proposed Package": proposed_package,
                "Adoption Stage": adoption_stage,
                "Current Seats": current_seats,
                "Proposed Seats": proposed_seats,
                "Strategy Context": strategy_context,
                "Value Proposition": value_prop,
                "Strategy Delivery": strategy_delivery,
                "Challenges": challenges,
                "Insights Needs": insights_needs,
                "Additional Notes": additional_notes,
                "Proposal Format": proposal_format,
                "Proposal Length": proposal_length,
                "Pricing Details": pricing_details,
                "Customer Success": customer_success,
                "Service Packages": service_packages,
                "Appendix": appendix,
                "Case Study": case_study,
                "Graphics": graphics,
                "Customer Name in Proposal": customer_name,
                "Proposal Scenario": Proposal_Scenario,
                "Unique Aspects": unique_aspects,
                "Internal Challenges": internal_challenges,
                "Start Date": str(start_date),
                "Roles": roles,
                "Competitors": competitors,
            }
            st.json(form_data) 
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(form_data, f, ensure_ascii=False, indent=4)

       

