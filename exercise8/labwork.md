Exploring Cocoli
----------------

rmarkdown::render("untitled2",output\_format = "md\_document")

    cocoli_dat<-read.table("/home/eeb177-student/Desktop/eeb274/class-assignments/class-assignments/21-Feb/cocoli.txt",header = TRUE)
    head(cocoli_dat)

    ##      tag spcode   x   y dbh1 dbh2 dbh3 recr1 recr2 recr3 pom1 pom2 pom3
    ## 1 000001 PROTTE 3.0 0.9  171  267  277     A     A     A    1    2    2
    ## 2 000002 COCCPA 0.1 0.6   13   14   17     A     A     A    1    1    1
    ## 3 000003 EUGEPR 1.3 2.3   26   33   39     A     A     A    1    2    2
    ## 4 000004 PROTTE 2.2 3.4   10   17   19     A     A     A    1    1    1
    ## 5 000005 CLAVME 3.5 3.7   14   15   15     A     A     A    1    1    1
    ## 6 000006 PROTTE 4.3 4.7   12   26   25     A     A     A    1    2    2
    ##   code1 code2 code3 mult1 mult2 mult3      date1      date2      date3
    ## 1     *     *     *     1     1     1 11/02/1994 11/11/1997 11/23/1998
    ## 2     *     *     *     1     1     1 11/02/1994 11/11/1997 11/23/1998
    ## 3     M     M     M     2     2     2 11/02/1994 11/11/1997 11/23/1998
    ## 4     *     *     *     1     1     1 11/02/1994 11/11/1997 11/23/1998
    ## 5    ML    ML     M     2     2     2 11/02/1994 11/11/1997 11/23/1998
    ## 6     *     *     M     1     1     2 11/02/1994 11/11/1997 11/23/1998

    sizes_in_94 <- cocoli_dat$dbh1
    names(sizes_in_94) <- cocoli_dat$tag
    sizes_in_97 <- cocoli_dat$dbh2
    sizes_in_98 <- cocoli_dat$dbh3
    which(sizes_in_94 == 171)

    ## 000001 006705 007074 
    ##      1   4236   4604

    library(ggplot2)
    ggplot(cocoli_dat) + geom_histogram(aes(dbh1)) + geom_histogram(aes(dbh2))+ ggtitle("distribution sizes '94") 

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](labwork_files/figure-markdown_strict/unnamed-chunk-2-1.png)

    housing <- read.csv("dataSets/landdata-states.csv")
    head(housing[1:5])

    ##   State region    Date Home.Value Structure.Cost
    ## 1    AK   West 2010.25     224952         160599
    ## 2    AK   West 2010.50     225511         160252
    ## 3    AK   West 2009.75     225820         163791
    ## 4    AK   West 2010.00     224994         161787
    ## 5    AK   West 2008.00     234590         155400
    ## 6    AK   West 2008.25     233714         157458

    hist(housing$Home.Value)

![](labwork_files/figure-markdown_strict/unnamed-chunk-3-1.png)

    ggplot(housing, aes(x = Home.Value)) +
      geom_histogram()

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](labwork_files/figure-markdown_strict/unnamed-chunk-4-1.png)

    plot(Home.Value ~ Date,
         data=subset(housing, State == "MA"))
    points(Home.Value ~ Date, col="blue",
           data=subset(housing, State == "TX"))
    legend(1975, 400000,
           c("MA", "TX"), title="State",
           col=c("black", "blue"),
           pch=c(1, 1))

![](labwork_files/figure-markdown_strict/unnamed-chunk-5-1.png)

    ggplot(subset(housing, State %in% c("MA", "TX")),
           aes(x=Date,
               y=Home.Value,
               color=State))+
      geom_point()

![](labwork_files/figure-markdown_strict/unnamed-chunk-6-1.png)

    hp2001Q1 <- subset(housing, Date == 2001.25) 
    ggplot(hp2001Q1,
           aes(y = Structure.Cost, x = Land.Value)) +
      geom_point()

![](labwork_files/figure-markdown_strict/unnamed-chunk-7-1.png)

    hp2001Q1$pred.SC <- predict(lm(Structure.Cost ~ log(Land.Value), data = hp2001Q1))

    p1 <- ggplot(hp2001Q1, aes(x = log(Land.Value), y = Structure.Cost))

    p1 + geom_point(aes(color = Home.Value)) +
      geom_line(aes(y = pred.SC))

![](labwork_files/figure-markdown_strict/unnamed-chunk-8-1.png)

    p1 +
      geom_point(aes(color = Home.Value)) +
      geom_smooth()

    ## `geom_smooth()` using method = 'loess'

![](labwork_files/figure-markdown_strict/unnamed-chunk-9-1.png)

    p1 + 
      geom_text(aes(label=State), size = 3)

![](labwork_files/figure-markdown_strict/unnamed-chunk-10-1.png)

    library("ggrepel")
    p1 + 
      geom_point() + 
      geom_text_repel(aes(label=State), size = 3)

![](labwork_files/figure-markdown_strict/unnamed-chunk-11-1.png)

    p1 +
      geom_point(aes(size = 2),# incorrect! 2 is not a variable
                 color="red") # this is fine -- all points red

![](labwork_files/figure-markdown_strict/unnamed-chunk-12-1.png)

    p1 +
      geom_point(aes(color=Home.Value, shape = region))

    ## Warning: Removed 1 rows containing missing values (geom_point).

![](labwork_files/figure-markdown_strict/unnamed-chunk-13-1.png)

    dat <- read.csv("dataSets/EconomistData.csv")
    head(dat)

    ##   X     Country HDI.Rank   HDI CPI            Region
    ## 1 1 Afghanistan      172 0.398 1.5      Asia Pacific
    ## 2 2     Albania       70 0.739 3.1 East EU Cemt Asia
    ## 3 3     Algeria       96 0.698 2.9              MENA
    ## 4 4      Angola      148 0.486 2.0               SSA
    ## 5 5   Argentina       45 0.797 3.0          Americas
    ## 6 6     Armenia       86 0.716 2.6 East EU Cemt Asia

    ggplot(dat, aes(x = CPI, y = HDI, size = HDI.Rank)) + geom_point(color='blue')

![](labwork_files/figure-markdown_strict/unnamed-chunk-14-1.png)

    args(geom_histogram)

    ## function (mapping = NULL, data = NULL, stat = "bin", position = "stack", 
    ##     ..., binwidth = NULL, bins = NULL, na.rm = FALSE, show.legend = NA, 
    ##     inherit.aes = TRUE) 
    ## NULL

    args(stat_bin)

    ## function (mapping = NULL, data = NULL, geom = "bar", position = "stack", 
    ##     ..., binwidth = NULL, bins = NULL, center = NULL, boundary = NULL, 
    ##     breaks = NULL, closed = c("right", "left"), pad = FALSE, 
    ##     na.rm = FALSE, show.legend = NA, inherit.aes = TRUE) 
    ## NULL

    p2 <- ggplot(housing, aes(x = Home.Value))
    p2 + geom_histogram()

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](labwork_files/figure-markdown_strict/unnamed-chunk-15-1.png)

    p2 + geom_histogram(stat = "bin", binwidth=4000)

![](labwork_files/figure-markdown_strict/unnamed-chunk-16-1.png)

    housing.sum <- aggregate(housing["Home.Value"], housing["State"], FUN=mean)
    rbind(head(housing.sum), tail(housing.sum))

    ##    State Home.Value
    ## 1     AK  147385.14
    ## 2     AL   92545.22
    ## 3     AR   82076.84
    ## 4     AZ  140755.59
    ## 5     CA  282808.08
    ## 6     CO  158175.99
    ## 46    VA  155391.44
    ## 47    VT  132394.60
    ## 48    WA  178522.58
    ## 49    WI  108359.45
    ## 50    WV   77161.71
    ## 51    WY  122897.25

    ggplot(housing.sum, aes(x=State, y=Home.Value)) + 
      geom_bar(stat="identity")

![](labwork_files/figure-markdown_strict/unnamed-chunk-18-1.png)

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(size = 2, color='blue') + geom_smooth(method = "lm")

![](labwork_files/figure-markdown_strict/unnamed-chunk-19-1.png)

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(size = 2, color='blue') + geom_line() + stat_smooth()

    ## `geom_smooth()` using method = 'loess'

![](labwork_files/figure-markdown_strict/unnamed-chunk-20-1.png)

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(size = 2, color='blue') + geom_smooth(span = 1/3)

    ## `geom_smooth()` using method = 'loess'

![](labwork_files/figure-markdown_strict/unnamed-chunk-21-1.png)

    p3 <- ggplot(housing,
                 aes(x = State,
                     y = Home.Price.Index)) + 
            theme(legend.position="top",
                  axis.text=element_text(size = 6))
    (p4 <- p3 + geom_point(aes(color = Date),
                           alpha = 0.5,
                           size = 1.5,
                           position = position_jitter(width = 0.25, height = 0)))

![](labwork_files/figure-markdown_strict/unnamed-chunk-22-1.png)

    p4 + scale_x_discrete(name="State Abbreviation") +
      scale_color_continuous(name="",
                             breaks = c(1976, 1994, 2013),
                             labels = c("'76", "'94", "'13"))

![](labwork_files/figure-markdown_strict/unnamed-chunk-23-1.png)

    p4 +
      scale_x_discrete(name="State Abbreviation") +
      scale_color_continuous(name="",
                             breaks = c(1976, 1994, 2013),
                             labels = c("'76", "'94", "'13"),
                             low = "blue", high = "red")

![](labwork_files/figure-markdown_strict/unnamed-chunk-24-1.png)

    p4 +
      scale_color_continuous(name="",breaks=c(1976,1994,2013),labels=c("'76","'94","'13"),low = "blue", high = "red")

![](labwork_files/figure-markdown_strict/unnamed-chunk-25-1.png)

    p4 +
      scale_color_gradient2(name="",
                            breaks = c(1976, 1994, 2013),
                            labels = c("'76", "'94", "'13"),
                            low = "blue",
                            high = "red",
                            mid = "gray60",
                            midpoint = 1994)

![](labwork_files/figure-markdown_strict/unnamed-chunk-26-1.png)

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(aes(color = dat$Region),
                           alpha = 0.5,
                           size = 1.5,
                           position = position_jitter(width = 0.25, height = 0))

![](labwork_files/figure-markdown_strict/unnamed-chunk-27-1.png)

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(aes(color = Region), shape = 21, fill = "white",
                           size = 1.5,
                           position = position_jitter(width = 0.25, height = 0)) + scale_color_manual(values = c("red","blue","orange","darkblue","yellow","orange4"),labels = c("Americas", "Asia Pacific", "Eastern Europe/Central Asia","Europian Union/Western Europe","Middle East/Northern Africa","Sub-Saharan Africa")) + labs(y = "Human Development Index", x = "Corruption Perception Index") + theme(legend.position = "top",legend.direction = "horizontal") + geom_text(aes(label = Country),check_overlap = TRUE)

![](labwork_files/figure-markdown_strict/unnamed-chunk-28-1.png)

    p5 <- ggplot(housing, aes(x = Date, y = Home.Value))
    p5 + geom_line(aes(color = State))

![](labwork_files/figure-markdown_strict/unnamed-chunk-29-1.png)

    (p5 <- p5 + geom_line() +
       facet_wrap(~State, ncol = 10))

![](labwork_files/figure-markdown_strict/unnamed-chunk-30-1.png)

    p5 + theme_linedraw()

![](labwork_files/figure-markdown_strict/unnamed-chunk-31-1.png)

    p5 + theme_minimal() +
      theme(text = element_text(color = "turquoise"))

![](labwork_files/figure-markdown_strict/unnamed-chunk-32-1.png)

    theme_new <- theme_bw() +
      theme(plot.background = element_rect(size = 1, color = "blue", fill = "black"),
            text=element_text(size = 12, family = "Serif", color = "ivory"),
            axis.text.y = element_text(colour = "purple"),
            axis.text.x = element_text(colour = "red"),
            panel.background = element_rect(fill = "pink"),
            strip.background = element_rect(fill = "orange"))

    p5 + theme_new

![](labwork_files/figure-markdown_strict/unnamed-chunk-33-1.png)

    country_col = c("Afghanistan", "Congo", "Sudan", "Myanmar", "Iraq", "India", "Venezuela", "Russia", "Argentina", "Greece", "Brazil", "Italy", "China", "South Africa", "Rwanda", "Bhutan", "Cape Verde", "Botswana", "Italy", "Spain", "France", "US", "Germany", "Britain", "Barbados", "Japan", "Norway", "Singapore", "New Zealand")

    plot_country <- rep(NA,173)
    out_which <- which (dat$Country %in% country_col)
    country_names <- as.character(dat$Country)
    plot_country[out_which] <- country_names[out_which]
    plot_country

    ##   [1] "Afghanistan"  NA             NA             NA            
    ##   [5] "Argentina"    NA             NA             NA            
    ##   [9] NA             NA             NA             NA            
    ##  [13] "Barbados"     NA             NA             NA            
    ##  [17] "Bhutan"       NA             NA             "Botswana"    
    ##  [21] "Brazil"       "Britain"      NA             NA            
    ##  [25] NA             NA             NA             NA            
    ##  [29] "Cape Verde"   NA             NA             NA            
    ##  [33] "China"        NA             NA             "Congo"       
    ##  [37] NA             NA             NA             NA            
    ##  [41] NA             NA             NA             NA            
    ##  [45] NA             NA             NA             NA            
    ##  [49] NA             NA             NA             NA            
    ##  [53] NA             NA             NA             "France"      
    ##  [57] NA             NA             NA             "Germany"     
    ##  [61] NA             "Greece"       NA             NA            
    ##  [65] NA             NA             NA             NA            
    ##  [69] NA             NA             NA             "India"       
    ##  [73] NA             NA             "Iraq"         NA            
    ##  [77] NA             "Italy"        NA             "Japan"       
    ##  [81] NA             NA             NA             NA            
    ##  [85] NA             NA             NA             NA            
    ##  [89] NA             NA             NA             NA            
    ##  [93] NA             NA             NA             NA            
    ##  [97] NA             NA             NA             NA            
    ## [101] NA             NA             NA             NA            
    ## [105] NA             NA             NA             NA            
    ## [109] NA             "Myanmar"      NA             NA            
    ## [113] NA             "New Zealand"  NA             NA            
    ## [117] NA             "Norway"       NA             NA            
    ## [121] NA             NA             NA             NA            
    ## [125] NA             NA             NA             NA            
    ## [129] NA             "Russia"       "Rwanda"       NA            
    ## [133] NA             NA             NA             NA            
    ## [137] NA             NA             NA             "Singapore"   
    ## [141] NA             NA             NA             "South Africa"
    ## [145] "Spain"        NA             "Sudan"        NA            
    ## [149] NA             NA             NA             NA            
    ## [153] NA             NA             NA             NA            
    ## [157] NA             NA             NA             NA            
    ## [161] NA             NA             NA             NA            
    ## [165] NA             NA             NA             NA            
    ## [169] NA             "Venezuela"    NA             NA            
    ## [173] NA

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(aes(color = Region), shape = 21, fill = "white",
                           size = 1.5,
                           position = position_jitter(width = 0.25, height = 0)) + scale_color_manual(values = c("red","blue","orange","darkblue","yellow","orange4"),labels = c("Americas", "Asia Pacific", "Eastern Europe/Central Asia","Europian Union/Western Europe","Middle East/Northern Africa","Sub-Saharan Africa")) + labs(y = "Human Development Index", x = "Corruption Perception Index") + theme(legend.position = "top",legend.direction = "horizontal") + geom_smooth(se = FALSE, color = "red") +  geom_text_repel(dat = subset(dat,Country==plot_country), aes(label = Country), size = 3)

    ## `geom_smooth()` using method = 'loess'

![](labwork_files/figure-markdown_strict/unnamed-chunk-36-1.png)
