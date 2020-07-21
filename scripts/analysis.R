setwd("~/Desktop/j_league/scripts")

library(tidyverse)

data <- read_csv('../data/data.csv')
data_detail <- read_csv('../data/data_detail.csv')

data <- data %>% 
  filter(year >= 2000)

data_all <- cbind(data, data_detail) %>% tibble()

my_theme <-
  theme_bw(base_family = "HiraKakuProN-W3") + 
  theme(axis.text = element_text(size = 10, angle = 45), legend.position="none",
        axis.title = element_text(size = 20), axis.ticks.length=unit(0.5, "cm"))
theme_set(my_theme) # set theme

data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>% 
  group_by(whether) %>% 
  summarise(
    mean_score = mean(total_score)
  ) %>% 
  ggplot() +
  geom_bar(aes(x = whether, y = mean_score), stat = 'identity')

data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>% 
  ggplot(aes(x = whether, y = total_score)) +
  geom_boxplot()

data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>% 
  ggplot(aes(x = temperature, y = total_score)) +
  geom_point() +
  geom_smooth(method = 'lm')
  
  
data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>% 
  ggplot(aes(x = total_score)) +
  geom_histogram(bins = 30)

p1 <- 
  data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>% 
  group_by(whether) %>% 
  summarise(
    mean_score = mean(total_score)
  ) %>% 
  ggplot() +
  geom_point(aes(x = whether, y = mean_score), color = 'red', size = 3)

p2 <-
  data_all %>% 
  mutate(total_score = as.integer(home_scores) + as.integer(away_scores)) %>%
  geom_jitter(mapping = aes(x = whether, y = total_score), alpha = 0.2)

p1 + p2

