str(binary)

col_names <- names(binary)
binary[,col_names] <- lapply(binary[,col_names] , factor)

library(arules)
library(arulesViz)

# Generate rules using apriori()
.all <- apriori(binary, parameter=list(support=0.01, confidence=0.5))
inspect(.all)

# Rules when when people are admitted
.all <- apriori(binary,
                     parameter = list(support=0.01, confidence=0.5),
                     appearance = list(rhs = c("admit=1"), default="lhs"))

# Keep to three decimal places
quality(rules.all) <- round(quality(rules.all), digits = 3)

# Remove redundant rules
subset.matrix <- is.subset(rules.all, rules.all)
subset.matrix[lower.tri(subset.matrix, diag = T)] <- NA
redundant <- colSums(subset.matrix, na.rm = T) >= 1
rules.pruned <- rules.all[!redundant]

inspect(rules.pruned)

# Visulize the rules

plot(rules.all)
# plot(rules.all, method = "grouped")
# plot(rules.all, method = "graph")

# Rules when when people are not admitted
rules.all <- apriori(binary,
                     parameter = list(support=0.01, confidence=0.5),
                     appearance = list(rhs = c("admit=0"), default="lhs"))

inspect(rules.all)
