--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Homebrew)
-- Dumped by pg_dump version 15.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: award; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.award (
    organizationname character varying(255),
    spid integer
);


ALTER TABLE public.award OWNER TO malavikanair;

--
-- Name: coach; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.coach (
    spid integer,
    duration integer
);


ALTER TABLE public.coach OWNER TO malavikanair;

--
-- Name: organization; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.organization (
    orgid integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.organization OWNER TO malavikanair;

--
-- Name: owner; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.owner (
    spid integer,
    networth numeric(12,2),
    boughtyear integer
);


ALTER TABLE public.owner OWNER TO malavikanair;

--
-- Name: playedfor; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.playedfor (
    teamid integer,
    spid integer NOT NULL,
    weight numeric(5,2),
    salary numeric(12,2)
);


ALTER TABLE public.playedfor OWNER TO malavikanair;

--
-- Name: player; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.player (
    spid integer,
    picture character varying(2083),
    "position" character varying(50),
    weight numeric(5,2)
);


ALTER TABLE public.player OWNER TO malavikanair;

--
-- Name: sportsperson; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.sportsperson (
    spid integer NOT NULL,
    name character varying(255),
    birthday date,
    college character varying(255)
);


ALTER TABLE public.sportsperson OWNER TO malavikanair;

--
-- Name: team; Type: TABLE; Schema: public; Owner: malavikanair
--

CREATE TABLE public.team (
    teamid integer,
    colors character varying(255),
    city character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.team OWNER TO malavikanair;

--
-- Data for Name: award; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.award (organizationname, spid) FROM stdin;
AP Most Valuable Player of The Year	1
AP Most Valuable Player of The Year	2
AP Offensive Rookie of the Year	22
\.


--
-- Data for Name: coach; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.coach (spid, duration) FROM stdin;
4	2
17	2
20	7
\.


--
-- Data for Name: organization; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.organization (orgid, name) FROM stdin;
1	Walton Payton Man of The Year
2	AP Most Valuable Player
3	AP Coach of the Year
4	AP Defensive Player of the Year
5	AP Offensive Rookie of the Year
\.


--
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.owner (spid, networth, boughtyear) FROM stdin;
13	20000000.00	2006
14	111000000.00	1994
5	74000000.00	2002
18	650000000.00	2023
21	157000000.00	1995
\.


--
-- Data for Name: playedfor; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.playedfor (teamid, spid, weight, salary) FROM stdin;
101	1	240.00	52650000.00
102	6	225.00	6000000.00
103	8	220.00	160000000.00
101	9	195.00	1612625.00
101	10	204.00	1623802.00
101	11	301.00	750000.00
101	12	240.00	948444.00
106	15	220.00	1187500.00
104	16	206.00	245000000.00
103	19	243.00	9125000.00
108	22	192.00	5138502.00
105	23	315.00	5250000.00
102	24	205.00	4300000.00
\.


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.player (spid, picture, "position", weight) FROM stdin;
6	\N	Running Back	225.00
7	\N	Running Back	232.00
9	\N	Wide Reciever	195.00
8	\N	Quarterback	220.00
10	\N	Running Back	204.00
2	\N	Quarterback	225.00
11	\N	Guard	301.00
12	\N	Tight End	240.00
1	\N	Quarterback	240.00
16	\N	Quarterback	206.00
15	\N	Linebacker	220.00
19	\N	Tight End	243.00
22	\N	Wide Reciever	192.00
23	\N	Defensive Tackle	315.00
24	\N	Safety	205.00
\.


--
-- Data for Name: sportsperson; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.sportsperson (spid, name, birthday, college) FROM stdin;
1	Patrick Mahomes	1995-09-17	Texas Tech
2	Tom Brady	1977-03-20	Michigan
3	Michael Johnson	1982-01-10	Baylor
4	Arthur Smith	1982-05-27	North Carolina
5	Arthur Blank	1942-09-27	Babson Institute
6	Ezekiel Elliott	1995-07-22	Ohio State
7	Saquon Barkley	1997-02-09	Penn State
8	Matthew Stafford	1988-02-07	Georgia
9	Skyy Moore	2000-09-10	Western Michigan
10	Rashee Rice	2000-04-22	SMU
11	Mike Caliendo	1997-10-21	Western Michigan
12	Noah Gray	1999-04-30	Duke
13	Clark Hunt	1965-02-19	SMU
14	Robert Kraft	1941-06-05	Harvard
15	Dylan Cole	1995-12-07	Missouri State
16	Russell Wilson	1988-11-29	NC State
17	Sean Payton	1963-12-29	Eastern Illinois University
18	Rob Walton	1944-10-27	Columbia Law School
19	Tyler Higbee	1993-01-01	Western Kentucky
20	Sean McVay	1986-01-24	Miami University (OH)
21	Stan Kroenke	1947-07-29	University of Missouri
22	Garrett Wilson	2000-07-22	Ohio State University
23	Broderick Washington	1996-12-04	Texas Tech
24	Cody Davis	1989-06-06	Texas Tech
\.


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: malavikanair
--

COPY public.team (teamid, colors, city, name) FROM stdin;
101	Red,gold,White	Kansas City	Kansas City Chiefs
102	Blue,Red,Silver,White	Boston	New England Patriots
103	Blue,Yellow	Los Angeles	Los Angeles Rams
104	Orange, White and Navy Blue	Denver	Denver Broncos
105	Purple, Black, Mettalic Gold	Baltimore	Baltimore Ravens
106	Dark Navy, Orange	Chicago	Chicago Bears
107	Black, Gold	Pittsburgh	Pittsburgh Steelers
108	Green, Black, White	New York Metropolitan Area	New York Jets
\.


--
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (name);


--
-- Name: playedfor playedfor_pkey; Type: CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.playedfor
    ADD CONSTRAINT playedfor_pkey PRIMARY KEY (spid);


--
-- Name: sportsperson sportsperson_pkey; Type: CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.sportsperson
    ADD CONSTRAINT sportsperson_pkey PRIMARY KEY (spid);


--
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (name);


--
-- Name: coach coach_spid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_spid_fkey FOREIGN KEY (spid) REFERENCES public.sportsperson(spid);


--
-- Name: owner owner_spid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_spid_fkey FOREIGN KEY (spid) REFERENCES public.sportsperson(spid);


--
-- Name: player player_spid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: malavikanair
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_spid_fkey FOREIGN KEY (spid) REFERENCES public.sportsperson(spid);


--
-- PostgreSQL database dump complete
--

